# fishfry-tours
Technical assessment for IS27 competition with CITZ

## Backend

The backend is written in Python with a PostgreSQL database. I chose PostgreSQL because, with the PostGIS extension, it could allow for advanced location-based queries, if the app were to be expanded upon so that the boats' geographic coordinates could be monitored while they were out at sea. (But that is beyond the scope of this assignment.)

I've also implemented GraphQL for building out the API, and in particular used the `Strawberry-GraphQL` (https://github.com/strawberry-graphql/strawberry) Python library. Using GraphQL wasn't strictly necessary, especially for an API as small as this app's, but I've never used GraphQL before and wanted to learn something new. As a nice bonus, having a GraphQL endpoint for the app up and running earlier on in the development process was handy for testing the database connection and the logic of the Boat model schema.

I chose Python for the backend language because it's great and I love it.

## DevOps Pipeline

Since my source code is hosted in GitHub, I chose to use GitHub Actions and integrated with Heroku as my chosen cloud host. This decision was based mostly on the cost (free!).

## QA

### Unit tests (Pytest)

Unit tests have been written in `pytest`, covering all use cases of the correct usage of GraphQL (such as creating, deleting, or editing a boat), as well as some test cases for erroneous usage (such as trying to create 2 boats with the same name).

I wrote unit tests to assert the correct functionality of all GraphQL functions since they are the backbone of the API, and these unit tests run fine and pass when running locally. However, getting `pytest` to run as part of the pipeline proved problematic, and some developers might argue is unnecessary. In order for the unit tests to run, there needs to be a database engine available with the database schema already in place. This means that pytest can't be run as part of the GitHub Actions workflow, because there is no way to provision a test database within GitHub Actions.

The only other way to have Python unit tests run as part of the pipeline is to have them run on the cloud hosting service provider. In my case, I chose to host the app on Heroku, since I've used this platform in the past and it is the only cloud provider I know of that doesn't ask for billing information when using free-tier services. Heroku does provide a "Heroku CI" add-on to their "Pipeline" construct, which would allow for automated test runs, but this isn't available at the free-tier.

### Functional Testing

I would recommend the following strategies for performing functional testing of this app:

| Test | Strategy |
| --------| ---------|
| Main functions within app | Implement end-to-end (E2E) testing with a framework such as Cypress. Add unit tests for the front-end to ensure correct functionality of components. |
| Basic usability & accessibility | There are some automated tools that could be used to test accessibility; for example, there are browser extensions available that could be run on the web app to check for factors such as adequate contrast between colours, font sizing, screen reader setup, etc. Usability testing sessions with actual or potential users of the software would also be advisable. |
| Error conditions | Some error conditions can be accounted for with automated unit or E2E tests. However, since I, as the sole developer/designer, have a fixed idea in mind of how users would use the app, the error handling that I can account for in automated testing has limits. Usability testing sessions with actual users would be the best way to ensure that error conditions resulting from improper usage (either accidental or intentional) of the app are handled correctly. |

## Attributions

I closely followed this tutorial to learn how to use `Quart`, `hypercorn`, and `Strawberry-graphql`: https://github.com/rockyburt/Ketchup

Boat name ideas taken from https://skyaboveus.com/water-sports/boat-name-ideas
