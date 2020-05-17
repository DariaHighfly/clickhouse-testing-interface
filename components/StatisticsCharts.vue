<template>
    <div class="all-tests">
        <div class="row">
            <div class="column">
                <PieChart
                    :commitName="commits.rightCommit.commit"
                    :allTests="allQueries"
                    :failTests="runErrors.length"
                    :skippedTests="skippedTests.length">
                </PieChart>
                <TestStatistics
                    :allTests="allQueries"
                    :failTests="runErrors.length"
                    :skippedTests="skippedTests.length">
                </TestStatistics>
            </div>
            <HistoryTestsColumnChart
                :allTestsHistory="allTestsHistory">
            </HistoryTestsColumnChart>
        </div>
        <div class="row">
            <TimePerformanceColumnChart
                :timePerformance="timePerformance">
            </TimePerformanceColumnChart>
        </div>
        <div class="row">
            <UnstableTestsChart
                :unstableQueries="unstableQueries">
            </UnstableTestsChart>
        </div>
        <div class="row">
            <AllTestsTimeSpline
                :timePerformance="timePerformance"
                :allTestsHistory="allTestsHistory">
            </AllTestsTimeSpline>
        </div>
    </div>
</template>

<script>
import HistoryTestsColumnChart from "./HistoryTestsColumnChart"
import TimePerformanceColumnChart from "./TimePerformanceColumnChart"
import PieChart from "./PieChart"
import TestStatistics from "./TestStatistics"
import AllTestsTimeSpline from "./AllTestsTimeSpline"
import UnstableTestsChart from "./UnstableTestsChart"
import {mapGetters} from "vuex";

export default {
    name: "StatisticsCharts",
    components: {
        HistoryTestsColumnChart,
        PieChart,
        TestStatistics,
        TimePerformanceColumnChart,
        AllTestsTimeSpline,
        UnstableTestsChart
    },
    computed: {
        ...mapGetters({
            commits: "tests/getCommits",
            changes: "tests/getChanges",
            unstableQueries: "tests/getUnstableQueries",
            runErrors: "tests/getRunErrors",
            skippedTests: "tests/getSkippedTests",
            badTests: "tests/getBadTests",
            testTimes: "tests/getTestTimes",
            slowOnClientTests: "tests/getSlowOnClientTests",
            allQueries: "tests/getAllQueries",
            timePerformance: "tests/getTimePerformance",
            commitsHistory: "tests/getCommitsHistory",
        }),
        allTestsHistory()  {
            let commitsAllTests = [];
            this.commitsHistory.map(elem => {
                commitsAllTests.push({
                    commit: elem.commits.rightCommit,
                    allTests: elem.allQueries,
                    failTests: elem.runErrors.length,
                    skippedTests: elem.skipped.length,
                    timePerformance: elem.timePerformance
                });
            });
            commitsAllTests.sort((a,b) => {
                return (new Date(a.commit.date) - new Date(b.commit.date))
            });
            return commitsAllTests;
        }
    }
}
</script>

<style scoped>
    .all-tests {
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        align-items: flex-start;
        margin-bottom: 40px;
    }
    .row {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        align-items: flex-start;
    }
    .column {
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        align-items: flex-start;
    }
</style>
