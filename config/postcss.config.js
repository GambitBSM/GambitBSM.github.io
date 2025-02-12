const autoprefixer = require('autoprefixer');
const whitelister = require('purgecss-whitelister');
const purgecssImport = require('@fullhuman/postcss-purgecss');
const purgeCSSPlugin = purgecssImport.purgeCSSPlugin || purgecssImport.default || purgecssImport
const purgecss = purgeCSSPlugin({
      content: [
        './layouts/**/*.html',
        './content/**/*.md',
      ],
      safelist: [
        'lazyloaded',
        'table',
        'thead',
        'tbody',
        'tr',
        'th',
        'td',
        'h5',
        'alert-link',
        'container-xxl',
        'container-fluid',
        'offcanvas-backdrop',
        ...whitelister([
          './assets/scss/components/_alerts.scss',
          './assets/scss/components/_buttons.scss',
          './assets/scss/components/_code.scss',
          './assets/scss/components/_diagrams.scss',
          './assets/scss/components/_syntax.scss',
          './assets/scss/components/_search.scss',
          './assets/scss/common/_dark.scss',
          './node_modules/bootstrap/scss/_dropdown.scss',
          './node_modules/katex/dist/katex.css',
        ]),
      ],
    })




module.exports = {
  plugins: [
    autoprefixer(),
    purgecss,
  ],
}
