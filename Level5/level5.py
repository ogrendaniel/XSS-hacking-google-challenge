'''Mission Description
Cross-site scripting isn't just about correctly escaping data. Sometimes, attackers can do bad things even without injecting new elements into the DOM.
Mission Objective
Inject a script to pop up an alert() in the context of the application. '''

script = "https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('XSS');"