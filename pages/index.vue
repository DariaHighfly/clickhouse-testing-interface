<template>
    <div id="app">
        <Menu></Menu>
        <div>
            <div class="navbar">
                <Navbar/>
            </div>
            <div class="box">
                <StatisticsCharts/>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from "vuex";

    import Menu from "../components/Menu"
    import Navbar from "../components/Navbar"
    import StatisticsCharts from "../components/StatisticsCharts"

    export default {
        name: 'app',
        components: {
            Navbar,
            StatisticsCharts,
            Menu
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
        width: 100%;
        background-color: #f4f6f8;
    }
    .navbar {
        width: 100vw;
        color: black;
        padding: 10px 0 15px 0;
        background-color: #FFFFFF;
    }
    .box {
        padding: 0 20px 0 20px;
        overflow: scroll;
    }
</style>
