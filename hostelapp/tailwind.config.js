/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: [
    './templates/**/*.{html,js}',
    './static/src/*.{html,js}',
    './static/js/**/*.js',
    './node_modules/flowbite/**/*.js',

  ],
  theme: {
    colors:{
      sky:colors.violet
    },
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {"50":"#eff6ff","100":"#dbeafe","200":"#bfdbfe","300":"#93c5fd","400":"#60a5fa","500":"#3b82f6","600":"#2563eb","700":"#1d4ed8","800":"#1e40af","900":"#1e3a8a","950":"#172554","255":"#FF00FF"},
        fuchsia: {
          "50": "#fde0ef",
          "100": "#fbb6ce",
          "200": "#f8719d",
          "300": "#f43c63",
          "400": "#e30b5d",
          "500": "#c2185b",
          "600": "#a21caf",
          "700": "#861d95",
          "800": "#6d178b",
          "900": "#55117a",
          "950": "#3b075e"
        }

      }
    },
    fontFamily: {
      'body': [
    'Inter', 
    'ui-sans-serif', 
    'system-ui', 
    '-apple-system', 
    'system-ui', 
    'Segoe UI', 
    'Roboto', 
    'Helvetica Neue', 
    'Arial', 
    'Noto Sans', 
    'sans-serif', 
    'Apple Color Emoji', 
    'Segoe UI Emoji', 
    'Segoe UI Symbol', 
    'Noto Color Emoji'
  ],
      'sans': [
    'Inter', 
    'ui-sans-serif', 
    'system-ui', 
    '-apple-system', 
    'system-ui', 
    'Segoe UI', 
    'Roboto', 
    'Helvetica Neue', 
    'Arial', 
    'Noto Sans', 
    'sans-serif', 
    'Apple Color Emoji', 
    'Segoe UI Emoji', 
    'Segoe UI Symbol', 
    'Noto Color Emoji'
  ]
    }
  }
}

