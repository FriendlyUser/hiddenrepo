const { SpecReporter } = require('jasmine-spec-reporter');
const karma = require('karma');
const tsNode = require('ts-node');

// Combine Karma configuration
function karmaConfig(config) {
  config.set({
    basePath: '',
    frameworks: ['jasmine', '@angular/cli'],
    plugins: [
      require('karma-jasmine'),
      require('karma-chrome-launcher'),
      require('karma-jasmine-html-reporter'),
      require('karma-coverage-istanbul-reporter'),
      require('@angular/cli/plugins/karma')
    ],
    client: {
      clearContext: false // leave Jasmine Spec Runner output visible in browser
    },
    coverageIstanbulReporter: {
      reports: ['html', 'lcovonly'],
      fixWebpackSourcePaths: true
    },
    angularCli: {
      environment: 'dev'
    },
    reporters: ['progress', 'kjhtml'],
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['Chrome'],
    singleRun: false
  });
}

// Combine Protractor configuration
const protractorConfig = {
  allScriptsTimeout: 11000,
  specs: [
    './e2e/**/*.e2e-spec.ts'
  ],
  capabilities: {
    'browserName': 'chrome'
  },
  directConnect: true,
  baseUrl: 'http://localhost:4200/',
  framework: 'jasmine',
  jasmineNodeOpts: {
    showColors: true,
    defaultTimeoutInterval: 30000,
    print: function() {}
  },
  onPrepare() {
    tsNode.register({
      project: 'e2e/tsconfig.e2e.json'
    });
    jasmine.getEnv().addReporter(new SpecReporter({ spec: { displayStacktrace: true } }));
  }
};

// Main entry point
function main() {
  console.log("Running Karma...");
  
  // Start Karma Server
  const server = new karma.Server({ configFile: __dirname + '/karma.conf.js' }, function(exitCode) {
    console.log('Karma has exited with ' + exitCode);
    process.exit(exitCode);
  });
  
  server.start();

  // Set up Protractor and run
  console.log("Running Protractor...");
  const protractor = require('protractor/built/launcher');
  protractor.init('./protractor.conf.js').then(result => {
    console.log("Protractor finished execution.");
   }).catch(err => {
    console.error("Error executing Protractor:", err);
  });
}

// Run main function to start processes
main();
