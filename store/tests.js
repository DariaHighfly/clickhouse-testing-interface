import main_json from "../static/test_data/commit/json_to_send";
import commit_json_1 from "../static/test_data/commit_1/json_to_send";
import commit_json_2 from "../static/test_data/commit_2/json_to_send";
import commit_json_3 from "../static/test_data/commit_3/json_to_send";
import commit_json_4 from "../static/test_data/commit_4/json_to_send";
import commit_json_5 from "../static/test_data/commit_5/json_to_send";
import commit_json_6 from "../static/test_data/commit_6/json_to_send";
import commit_json_7 from "../static/test_data/commit_7/json_to_send";
import commit_json_8 from "../static/test_data/commit_8/json_to_send";
import commit_json_9 from "../static/test_data/commit_9/json_to_send";
import commit_json_10 from "../static/test_data/commit_10/json_to_send";
import commit_json_11 from "../static/test_data/commit_11/json_to_send";
import commit_json_12 from "../static/test_data/commit_12/json_to_send";
import commit_json_13 from "../static/test_data/commit_13/json_to_send";
import commit_json_14 from "../static/test_data/commit_14/json_to_send";
import commit_json_15 from "../static/test_data/commit_15/json_to_send";

export const state = () => ({
    currentCommitInfo: {
        commits: main_json.commits,
        changes: main_json.changes,
        unstableQueries: main_json.unstableQueries,
        runErrors: main_json.runErrors,
        skipped: main_json.skipped,
        badTests: main_json.badTests,
        testTimes: main_json.testTimes,
        slowOnClient: main_json.slowOnClient,
        allQueries: main_json.allQueries,
        timePerformance: main_json.timePerformance,
        reportErrors: main_json.reportErrors
    },
    commitsHistory: [
        commit_json_1,
        commit_json_2,
        commit_json_3,
        commit_json_4,
        commit_json_5,
        commit_json_6,
        commit_json_7,
        commit_json_8,
        commit_json_9,
        commit_json_10,
        commit_json_11,
        commit_json_12,
        commit_json_13,
        commit_json_14,
        commit_json_15
    ]
});

export const getters = {
    getAllTestInfo: (state) => {
        return state.currentCommitInfo;
    },
    getCommitsHistory: (state) => {
        return state.commitsHistory;
    },
    getCommits: (state) => {
        return state.currentCommitInfo.commits;
    },
    getChanges: (state) => {
        return state.currentCommitInfo.changes;
    },
    getUnstableQueries: (state) => {
        return state.currentCommitInfo.unstableQueries;
    },
    getRunErrors: (state) => {
        return state.currentCommitInfo.runErrors;
    },
    getSkippedTests: (state) => {
        return state.currentCommitInfo.skipped;
    },
    getBadTests: (state) => {
        return state.currentCommitInfo.badTests;
    },
    getTestTimes: (state) => {
        return state.currentCommitInfo.testTimes;
    },
    getSlowOnClientTests: (state) => {
        return state.currentCommitInfo.slowOnClient;
    },
    getAllQueries: (state) => {
        return state.currentCommitInfo.allQueries;
    },
    getTimePerformance: (state) => {
        return state.currentCommitInfo.timePerformance;
    },
    getDataErrors: (state) => {
        return state.currentCommitInfo.reportErrors;
    },
};
