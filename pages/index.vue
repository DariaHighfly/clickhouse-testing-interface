<template>
    <div id="app">
        <div class="menu">
            <img class="main-logo" src="../assets/logo.svg">
            <div class="menu__list">
                <div class="menu__list__item"
                     v-on:click="changePage('dashboard')"
                     v-bind:class="{'menu__list__item-selected': (currentPage === 'dashboard')}">
                    <img class="menu__img" src="../assets/dashboard.png">
                    <p class="menu__text">Dashboard</p>
                </div>
                <div class="menu__list__item"
                     v-on:click="changePage('tables')"
                     v-bind:class="{'menu__list__item-selected': (currentPage === 'tables')}">
                    <img class="menu__img" src="../assets/tables.png">
                    <p class="menu__text">Tables</p>
                </div>
                <div class="menu__list__item"
                     v-on:click="changePage('queries')"
                     v-bind:class="{'menu__list__item-selected': (currentPage === 'queries')}">
                    <img class="menu__img" src="../assets/queries.png">
                    <p class="menu__text">All Queries</p>
                </div>
                <div class="menu__list__item"
                     v-on:click="changePage('logs')"
                     v-bind:class="{'menu__list__item-selected': (currentPage === 'logs')}">
                    <img class="menu__img" src="../assets/log.png">
                    <p class="menu__text">Logs</p>
                </div>
                <div class="menu__list__item"
                     v-on:click="changePage('download')"
                     v-bind:class="{'menu__list__item-selected': (currentPage === 'download')}">
                    <img class="menu__img" src="../assets/download.png">
                    <p class="menu__text">Download</p>
                </div>
            </div>
        </div>
        <div class="app__page">
            <div class="navbar">
                <Navbar/>
            </div>
            <div class="box" v-if="currentPage === 'dashboard'">
                <StatisticsCharts/>
            </div>
            <div class="box" v-if="currentPage === 'tables'">
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
            <div class="box" v-if="currentPage === 'queries'">
                <AllQueries
                    :allQueries="allQueries">
                </AllQueries>
            </div>
            <div class="box" v-if="currentPage === 'logs'">
                <Logs
                    :compareLog="compareLog">
                </Logs>
            </div>
            <div class="box" v-if="currentPage === 'download'">
                <Download
                    :commitName="commits.rightCommit.commit">
                </Download>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from "vuex";

    import Menu from "../components/Menu"
    import Navbar from "../components/Navbar"
    import StatisticsCharts from "../components/StatisticsCharts"
    import StatisticsAllTables from "../components/StatisticsAllTables"
    import AllQueries from "../components/AllQueries"
    import Logs from "../components/Logs"
    import Download from "../components/Download"

    export default {
        name: 'app',
        components: {
            Navbar,
            StatisticsCharts,
            Menu,
            StatisticsAllTables,
            AllQueries,
            Logs,
            Download
        },
        data() {
            return {
                currentPage: "dashboard"
            }
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
                compareLog: "tests/getCompareLog"
            })
        },
        methods: {
            changePage(page) {
                this.currentPage = page;
            }
        }
    }
</script>

<style>
    body {
        margin: 0;
        width: 100%;
        background-color: #f4f6f8;
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
    .app__page {
        width: 100%;
    }
    .navbar {
        width: 100%;
        padding: 10px 0 15px 0;
        background-color: #FFFFFF;
    }
    .box {
        padding: 0 20px 0 20px;
        overflow: scroll;
    }


    .menu {
        display: flex;
        flex-direction: column;
        background-color: #FFFFFF;
        transition: 0.5s;
    }
    .main-logo {
        height: 50px;
        width: auto;
        margin: 20px 0 0 0;
    }
    .menu__list {
        margin: 17px 0 0 0;
    }
    .menu__list__item {
        margin: 0;
        padding: 15px 10px 15px 10px;
        cursor: pointer;
    }
    .menu__list__item-selected {
        background-color: #98c807;
    }
    .menu__img {
        height: 35px;
        width: auto;
    }
    .menu__list a {
        text-decoration: none;
        font-size: 16px;
        color: #000000;
        display: block;
        transition: 0.3s;
    }
    .menu__text {
        text-decoration: none;
        font-size: 16px;
        color: #000000;
        margin: 0;
    }
</style>
