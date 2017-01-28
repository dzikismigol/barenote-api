## BareNote API 
[![Build Status](https://travis-ci.org/marszczybrew/barenote-api.svg?branch=master)](https://travis-ci.org/marszczybrew/barenote-api)
[![Code Climate](https://codeclimate.com/github/marszczybrew/barenote-api/badges/gpa.svg)](https://codeclimate.com/github/marszczybrew/barenote-api)

#### SDK
There is one [SDK in PHP](https://github.com/dzikismigol/barenote-sdk-php)

#### Tests
All tests are stored in `/test`, they use [PyRestTest](https://github.com/svanoort/pyresttest/) library. So far, they are defined for the following endpoints:
 - [x] `/api/note` - it has to be decided if there will be option to choose _public_ or _private_ note type, or which will be enforced globally
 - [x] `/api/category` - individual for each user, contains a collection of user notes
 - [x] `/api/tag` - tags assignable to notes, common throughout the whole api
 - [x] `/api/login` - auth endpoint, returns JWT tokens generated with help of [PyJWT](https://github.com/jpadilla/pyjwt) library
