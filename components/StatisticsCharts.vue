<template>
    <div class="all-tests">
        <div class="row">
            <PieChart
                :commitName="commits.rightCommit.commit"
                :allTests="allQueries"
                :failTests="runErrors.length"
                :skippedTests="skippedTests.length">
            </PieChart>
            <ColumnChart
                :allTestsHistory="allTestsHistory">
            </ColumnChart>
        </div>
        <div class="row">
            <TimePerformanceColumnChart
                :timePerformance="timePerformance">
            </TimePerformanceColumnChart>
        </div>
    </div>
</template>

<script>
import ColumnChart from "./ColumnChart";
import TimePerformanceColumnChart from "./TimePerformanceColumnChart"
import PieChart from "./PieChart";
import {mapGetters} from "vuex";

export default {
    name: "StatisticsCharts",
    components: {
        ColumnChart,
        PieChart,
        TimePerformanceColumnChart
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
    }
    .row {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        align-items: flex-start;
    }
</style>
