data = {
    "region": {
        "name": "Africa",
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": 5,
        "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614
}


def estimator(data):
    reportedCases = data["reportedCases"]
    timeToElapse = data["timeToElapse"]
    totalHospitalBeds = data["totalHospitalBeds"]
    periodType = data["periodType"]
    avgDailyIncomeInUSD = data["region"]["avgDailyIncomeInUSD"]
    avgDailyIncomePopulation = data["region"]["avgDailyIncomePopulation"]

    def timeInDays(timeToElapse, periodType):
        if (periodType == "days"):
            return timeToElapse
        elif (periodType == "weeks"):
            return timeToElapse * 7
        else:
            return timeToElapse * 30

    def getFactor(timeToElapse, periodType):
        return timeInDays(timeToElapse, periodType)/3

    factor = round(getFactor(timeToElapse, periodType))

    currentlyInfectedN = reportedCases * 10
    currentlyInfectedS = reportedCases * 50

    infectionsByRequestedTimeN = currentlyInfectedN * (2 ** factor)
    infectionsByRequestedTimeS = currentlyInfectedS * (2 ** factor)

    severeCasesByRequestedTimeN = round(infectionsByRequestedTimeN * 0.15)
    severeCasesByRequestedTimeS = round(infectionsByRequestedTimeS * 0.15)

    hospitalBedsByRequestedTimeN = round(
        totalHospitalBeds * 0.35 * severeCasesByRequestedTimeN
    )
    hospitalBedsByRequestedTimeS = round(
        totalHospitalBeds * 0.35 * severeCasesByRequestedTimeS
    )
    casesForICUByRequestedTimeN = round(0.05 * infectionsByRequestedTimeN)
    casesForICUByRequestedTimeS = round(0.05 * infectionsByRequestedTimeS)

    casesForVentilatorsByRequestedTimeN = round(
        0.02 * infectionsByRequestedTimeN)
    casesForVentilatorsByRequestedTimeS = round(
        0.02 * infectionsByRequestedTimeS)

    dollarsInFlightN = round(
        infectionsByRequestedTimeN * avgDailyIncomeInUSD * avgDailyIncomePopulation
    )
    dollarsInFlightS = round(
        infectionsByRequestedTimeS * avgDailyIncomeInUSD * avgDailyIncomePopulation
    )

    impact = {
        "currentlyInfected": currentlyInfectedN,
        "infectionsByRequestedTime": infectionsByRequestedTimeN,
        "severeCasesByRequestedTime": severeCasesByRequestedTimeN,
        "hospitalBedsByRequestedTime": hospitalBedsByRequestedTimeN,
        "casesForICUByRequestedTime": casesForICUByRequestedTimeN,
        "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeN,
        "dollarsInFlight": f"${dollarsInFlightN}"
    }

    severeImpact = {
        "currentlyInfected": currentlyInfectedS,
        "infectionsByRequestedTime": infectionsByRequestedTimeS,
        "severeCasesByRequestedTime": severeCasesByRequestedTimeS,
        "hospitalBedsByRequestedTime": hospitalBedsByRequestedTimeS,
        "casesForICUByRequestedTime": casesForICUByRequestedTimeS,
        "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeS,
        "dollarsInFlight": f"${dollarsInFlightS}"
    }

    return {
        "data": data,
        "impact": impact,
        "severeImpact": severeImpact
    }