<template>
    <div id="app">
        <Navbar/>
        <div class="box">
            <StatisticsCharts/>
            <StatisticsAllTables
                :commits="commits"
                :changes="changes"
                :unstableQueries="unstableQueries"
                :runErrors="runErrors"
                :skippedTests="skippedTests"
                :badTests="badTests"
                :testTimes="testTimes"
                :slowOnClientTests="slowOnClientTests">
            </StatisticsAllTables>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from "vuex";

    import Navbar from "~/components/Navbar"
    import StatisticsCharts from "~/components/StatisticsCharts"
    import StatisticsAllTables from "~/components/StatisticsAllTables"

    export default {
        name: 'app',
        components: {
            Navbar,
            StatisticsCharts,
            StatisticsAllTables,
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
            })
        }
    }
</script>

<style>
    #app {
        font-family: "Yandex Sans Display", sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 20px;
    }
    .box {
        padding: 0 20px 0 20px;
    }
</style>
