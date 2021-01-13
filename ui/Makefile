dist : main.js js_libs
	install src/index.html dist

main.js :
	npx tsc

js_libs :
	install node_modules/requirejs/require.js dist
	install -D node_modules/react/umd/react.production.min.js dist/react.js
	install node_modules/react-dom/umd/react-dom.production.min.js dist/react-dom.js

clean :
	rm -rf dist/*
