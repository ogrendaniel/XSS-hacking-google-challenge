'''Mission Description
As you've seen in the previous level, some common JS functions are execution sinks which means that they will cause the browser to execute any scripts that appear in their input. Sometimes this fact is hidden by higher-level APIs which use one of these functions under the hood.

The application on this level is using one such hidden sink.
Mission Objective
As before, inject a script to pop up a JavaScript alert() in the app.

Since you can't enter your payload anywhere in the application, you will have to manually edit the address in the URL bar below.'''

script = "#3' onerror='alert(1)"