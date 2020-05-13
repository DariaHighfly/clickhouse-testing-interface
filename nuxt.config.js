module.exports = {
    head: {
        title: 'ClickHouse testing interface',
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: 'Nuxt.js project' },
        ]
    },
    router: {
        base: './',
        mode: 'hash'
    },
    /*
    ** Customize the progress bar color
    */
    loading: { color: '#3B8070' },
    /*
    ** Build configuration
    */
    plugins: [{
        src: "~/plugins/vue-highcharts.js",
        ssr: true
    }],
    build: {
        /*
        ** Run ESLint on save
        */
        extend(config, ctx) {
            if(!ctx.isDev) {
                config.output.publicPath = '_nuxt/'
            }
        }
    },
}
