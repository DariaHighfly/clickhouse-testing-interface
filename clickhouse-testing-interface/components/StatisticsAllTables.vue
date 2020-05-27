<template>
    <div class="all-tables">
        <div class="commits">
            <p class="all-tables__title"
               v-bind:class="{'all-tables__title_hidden' : currentCommits.hidden}">
                {{currentCommits.name}}
            </p>
            <div class="all-tables__table-box">
                <table class="all-tables__table">
                    <thead>
                    <tr>
                        <th class="all-tables__table__title"></th>
                        <th class="all-tables__table__title" v-for="column in currentCommits.columns">
                            <div v-for="key in Object.keys(column)">
                                {{column[key]}}
                            </div>
                        </th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr class="all-tables__table__row" v-for="name in Object.keys(currentCommits.firstColumn)">
                        <td class="commits__column-title">{{currentCommits.firstColumn[name]}}</td>
                        <td class="all-tables__table__column">{{currentCommits.values.leftCommit[name]}}</td>
                        <td class="all-tables__table__column">{{currentCommits.values.rightCommit[name]}}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div v-for="table in Object.keys(tables)">
            <div v-if="tables[table].values.length">
                <div class="all-tables__title-box">
                    <p class="all-tables__title"
                       v-bind:class="{'all-tables__title_hidden' : tables[table].hidden}">
                        {{tables[table].name}}
                    </p>
                    <div v-on:click="changeTableVisability(table)">
                        <img class="all-tables__title-image active"
                             v-bind:class="{'all-tables__title-image_hidden' : tables[table].hidden}"
                             src="../assets/sort-img.png">
                    </div>
                </div>
                <div class="all-tables__table-box" v-bind:class="{'all-tables__table_visible' : !tables[table].hidden,
                 'all-tables__table_hidden' : tables[table].hidden}">
                    <table class="all-tables__table">
                        <thead>
                        <tr>
                            <th class="all-tables__table__title" v-for="column in tables[table].columns">
                                <div v-for="key in Object.keys(column)">
                                    <a class="active" v-on:click="sortBy(table, key)">
                                        {{column[key]}}
                                    </a>
                                </div>
                            </th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr class="all-tables__table__row" v-for="elem in tables[table].values">
                            <td class="all-tables__table__column" v-for="key in Object.keys(elem)">{{elem[key]}}</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "StatisticsAllTables",
        props: {
            commits: {
                type: Object,
                default: {}
            },
            changes: {
                type: Array,
                default: []
            },
            unstableQueries: {
                type: Array,
                default: []
            },
            runErrors: {
                type: Array,
                default: []
            },
            skippedTests: {
                type: Array,
                default: []
            },
            badTests: {
                type: Array,
                default: []
            },
            testTimes: {
                type: Array,
                default: []
            },
            slowOnClientTests: {
                type: Array,
                default: []
            },
        },
        data() {
            return {
                sortKey: "",
                reverse: 1,
                currentCommits: {
                    name: "Tested commits",
                    columns: [
                        { oldCommit: "Old" },
                        { newCommit: "New" },
                    ],
                    firstColumn: {
                        commit: "Commit",
                        author: "Author",
                        date: "Date",
                        info: "Info"},
                    values: {
                        leftCommit: {
                            commit: this.commits.leftCommit.commit,
                            author: this.commits.leftCommit.author,
                            date: new Date(this.commits.leftCommit.date),
                            info: this.commits.leftCommit.info,
                        },
                        rightCommit: {
                            commit: this.commits.rightCommit.commit,
                            author: this.commits.rightCommit.author,
                            date: new Date(this.commits.rightCommit.date),
                            info: this.commits.rightCommit.info,
                        },
                    },
                    hidden: false
                },
                tables: {
                    currentRunErrors: {
                        name: "Run errors",
                        columns: [
                            { testName: "Test" },
                            { error: "Error" }
                        ],
                        values: [...this.runErrors],
                        hidden: false
                    },
                    currentChanges: {
                        name: "Changes in performance",
                        columns: [
                            { oldTime: "Old, s" },
                            { newTime: "New, s" },
                            { relativeDifference: "Relative difference (new - old)/old" },
                            { quantiles: "Randomization distribution quantiles [5%, 50%, 95%, 99%]" },
                            { testName:  "Test" },
                            { query: "Query" }
                        ],
                        values: [...this.changes],
                        hidden: false
                    },
                    currentUnstableQueries: {
                        name: "Unstable queries",
                        columns: [
                            { oldTime: "Old, s" },
                            { newTime: "New, s" },
                            { relativeDifference: "Relative difference (new - old)/old" },
                            { quantiles: "Randomization distribution quantiles [5%, 50%, 95%, 99%]" },
                            { testName:  "Test" },
                            { query: "Query" }
                        ],
                        values:  this.unstableQueries.map(elem => {
                            let allowed = ["oldTime", "newTime", "relativeDifference", "quantiles", "testName", "query"];
                            let filtered = Object.keys(elem)
                                .filter(key => allowed.includes(key))
                                .reduce((obj, key) => {
                                    obj[key] = elem[key];
                                    return obj;
                                }, {});
                            return filtered;
                        }),
                        hidden: false
                    },
                    currentSkippedTests: {
                        name: "Skipped Tests",
                        columns: [
                            { testName: "Test" },
                            { reason: "Reason" }
                        ],
                        values: [...this.skippedTests],
                        hidden: false
                    },
                    currentBadTests: {
                        name: "Tests with most unstable queries",
                        columns: [
                            { testName: "Test" },
                            { unstable: "Unstable" },
                            { changedPerf: "Changed perf" },
                            { total: "Total not OK" }
                        ],
                        values: [...this.badTests],
                        hidden: false
                    },
                    currentTestTimes: {
                        name: "Test times",
                        columns: [
                            { testName: "Test" },
                            { wallClockTime: "Wall clock time, s" },
                            { clientTime: "Total client time, s" },
                            { total: "Total queries" },
                            { ignoredQueries:  "Ignored short queries" },
                            { longestQuery: "Longest query sum for all runs, s" },
                            { avgWallClockTime: "Avg wall clock time (sum for all runs), s" },
                            { shortestQuery: "Shortest query (sum for all runs), s" }
                        ],
                        values: [...this.testTimes],
                        hidden: false
                    },
                    currentSlowOnClientTests: {
                        name: "Slow On Client Tests",
                        columns: [
                            { clientTime: "Client time, s" },
                            { serverTime: "Server time, s" },
                            { ratio: "Ratio" },
                            { query: "Query" }
                        ],
                        values: [...this.slowOnClientTests],
                        hidden: false
                    }
                },
            }
        },
        methods: {
            sortBy(table, sortKey) {
                if (this.sortKey !== sortKey) {
                    this.reverse = 1;
                    this.sortKey = sortKey;
                }
                for (let i = 0; i !== this.tables[table].columns.length; ++i ) {
                    let key = Object.keys(this.tables[table].columns[i])[0];
                    if (sortKey === key) {
                        this.tables[table].values.sort((a, b) => {
                            if (typeof a[key] === "string") {
                                return this.reverse * (a[key]).localeCompare(b[key]);
                            } else if (typeof a[key] === "number") {
                                return this.reverse * (a[key] - b[key]);
                            } else if (Array.isArray(a[key])) {
                                for (let i = 0; i !== a[key].length; ++i) {
                                    if (a[key][i] !== b[key][i]) {
                                        return this.reverse * (a[key][i] - b[key][i]);
                                    }
                                }
                                return 0;
                            } else {
                                return 0;
                            }
                        });
                        this.reverse *= -1;
                        break;
                    }
                }
            },
            changeTableVisability(table) {
                this.tables[table].hidden = !this.tables[table].hidden;
            }
        }
    }
</script>

<style scoped>
    .active:hover {
        cursor: pointer;
    }
    .commits {
        margin: 0 0 20px 0;
    }
    .commits__column-title {
        color: #000000;
        background-color: #F8CD46;
        font-size: 15px;
        font-weight: bold;
        border-right: 2px solid #ddb342;
        border-bottom: 2px solid #ddb342;
        padding: 10px;
    }
    .all-tables {
        font-family: "Yandex Sans Display", sans-serif;
        color: black;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-bottom: 40px;
    }
    .all-tables__title {
        font-size: 23px;
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        margin: 20px 0 20px 0;
        transition: margin 0.15s linear;
    }
    .all-tables__title_hidden {
        margin: 5px 0 5px 0;
        transition: margin 0.15s linear;
    }
    .all-tables__title-image {
        height: 0.8em;
        width: auto;
        margin-left: 1em;
        transition: transform 0.15s linear;
    }
    .all-tables__title-image_hidden {
        -moz-transform: rotate(-90deg);
        -webkit-transform: rotate(-90deg);
        -o-transform: rotate(-90deg);
        -ms-transform: rotate(-90deg);
        transform: rotate(-90deg);
        transition: transform 0.15s linear;
    }
    .all-tables__table-box {
        background: #ffffff;
        border-radius: 2px;
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
    }
    .all-tables__table {
        background: #ffffff;
        border-collapse: collapse;
    }
    .all-tables__title-box {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
    }
    .all-tables__table__title {
        color: #000000;;
        background: #F8CD46;
        border-bottom: 4px solid #d3d3d3;
        font-size: 15px;
        font-weight: bold;
        padding: 10px;
        text-align: left;
        vertical-align: middle;
        border-right: 2px solid #ddb342;
    }
    .all-tables__table__title:last-child {
        border-right: none;
    }
    .all-tables__table__row {
        color: #282828;
        text-align: left;
        border-bottom: 2px solid #eaeaea;
    }
    .all-tables__table__row:last-child {
        border-right: none;
    }
    .all-tables__table__column {
        color: #282828;
        font-size: 14px;
        font-weight: normal;
        border-right: 2px solid #eaeaea;
        padding: 10px;
    }
    .all-tables__table__column:last-child {
        border-right: none;
    }
    table tr:nth-child(even) {
        background: #f7f7f7;
    }
    .all-tables__table_visible {
        height: auto;
        overflow: hidden;
        /*transition: height 1.5s linear;*/

    }
    .all-tables__table_hidden {
        height: 0;
        overflow: hidden;
        /*transition: height 1.5s linear;*/
    }
</style>
