var gulp = require('gulp');
var run = require('gulp-run');
var notify = require('gulp-notify');
var shell = require('gulp-shell')
 
gulp.task('test', function() {
    run('py.test --pep8').exec()
    .on('error', notify.onError({
        title: 'Doh!',
        message: '\nYour tests failed!\n',
        icon: __dirname + '/assets/fail.png'
    }))
    .pipe(notify({
        title: 'Woohoo!',
        message: '\nAll tests have returned green!\n',
        icon:  __dirname + '/assets/pass.png'
    }));
});
 
gulp.task('watch', function() {
    gulp.watch(['**/*.py', '!**/__init__.py'], ['test']);
});
 
gulp.task('default', ['test', 'watch']);