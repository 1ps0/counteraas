
# Counter As A Service

> A simple api with a simple front end for counting given strings

## API

> GET /c/<string>
> POST /c/<string>

--

# CounteraaS


## Basic premise

It's a ... counter.

`POST` increments the counter (starting at 1 after the first request), `GET` retrieves it. `POST` probably also returns the new value. If the record isn't found, it's either an error (404?) or `0`.

All params together make up the unique key, whether stored separately or not. They can probably be combined (and maybe hashed) for a Redis key, or something.


### Example

If I make a `POST` request with the params `{"date": "2018-09-24", "url": "/about"}`, it would store something like

Key | Value
:---|:-----
`"2018-09-24:/about"` | `1`

and return the `1`.

Another `POST` request with the same params would result in

Key | Value
:---|:-----
`"2018-09-24:/about"` | `2`

and return the `2`.

A `GET` request wtih matching params (`?date=2018-09-24&url=%2Fabout`) would return `2`.

Bonus feature: be able to decrement as well.


## Misc

- Hosting is probably Heroku + Redis.
- Stack is likely Flask + some Redis lib?
- Heroku has a Let's Encrypt checkbox.


---


**Everything below is probably best left for later.**


## Future enhancements

- public stats page
- auth
- separation by user
- client libraries
- crazy example uses (I can write up the `for` loop for shits and giggles if you want)


### Monetization

Example tiers:

1. Free: 1 counter up to `42`
2. Solo: 10 counters, no limit, $1/mo
3. Startup: 1,000 counters, no limit, $250/mo
4. Enterprise: call for pricing
