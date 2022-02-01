import React from "react";
import { Paper } from "@material-ui/core";
import { Typography } from "@material-ui/core";

export default function PageFooter() {

    return (
        <footer>
            <Paper>
                <Typography>
                see <a href="/graphql">Graph<em>i</em>QL</a> to interact with the GraphQL endpoint
                </Typography>
            </Paper>
        </footer>
    )
}