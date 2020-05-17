<template>
    <div id="app">
        <Menu></Menu>
        <div>
            <Navbar/>
            <div class="box">
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
    </div>
</template>

<script>
    import { mapGetters } from "vuex";
    import Menu from "../components/Menu"
    import Navbar from "../components/Navbar"
    import StatisticsAllTables from "~/components/StatisticsAllTables"

    export default {
        name: "tables",
        components: {
            Menu,
            Navbar,
            StatisticsAllTables
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

<style scoped>
    body {
        margin: 0;
    }
    #app {
        font-family: "Yandex Sans Display", sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        display: flex;
        flex-direction: row;
    }
    .box {
        width: 100%;
        padding: 0 20px 0 20px;
        background-color: #f4f6f8;
        overflow: scroll;
    }
</style>
