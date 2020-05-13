module.exports = {
    head: {
        title: 'ClickHouse testing interface',
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: 'Nuxt.js project' },
        ]
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
        publicPath: '_nuxt/',
        extend(config, { isDev, isClient }) {
            if (isDev && isClient) {
                config.module.rules.push({
                    enforce: 'pre',
                    test: /\.(js|vue)$/,
                    loader: 'eslint-loader',
                    exclude: /(node_modules)/,
                })
            }
        },
    },
}
