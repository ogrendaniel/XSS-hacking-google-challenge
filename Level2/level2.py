'''                     
                    Mission Description

Web applications often keep user data in server-side and, increasingly, client-side databases and later display 
it to users. No matter where such user-controlled data comes from, it should be handled carefully.

This level shows how easily XSS bugs can be introduced in complex apps.

                        Mission Objective
Inject a script to pop up an alert() in the context of the application. '''

# Solution
script = "<img src='x' onerror='alert('XSS')'> "

