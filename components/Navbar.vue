<template>
    <div class="navbar__block">
        <div class="navbar">
            <img class="navbar__img" src="../assets/logo.svg">
            <div>
                <p class="navbar__title">Performance</p>
                <p class="navbar__title">comparison of analytical DBMS</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Navbar"
    }
</script>

<style scoped>
    .navbar__block {
        width: 100%;
        color: black;
        margin-bottom: 60px;
        margin-left: 20px;
    }
    .navbar {
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .navbar__img {
        height: 40px;
        width: auto;
    }
    .navbar__title {
        font-family: "Yandex Sans Display", sans-serif;
        font-size: 25px;
        display: flex;
        justify-content: flex-start;
        padding: 0 0 0 20px;
        margin: 0;
    }
</style>
