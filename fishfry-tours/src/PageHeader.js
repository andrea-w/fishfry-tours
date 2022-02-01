import { AppBar, Toolbar } from "@material-ui/core"
import React from "react"

export default function PageHeader() {
    const display = () => {
        return <Toolbar>Fishfry Tours</Toolbar>
    }

    return (
        <header>
            <AppBar>{display()}</AppBar>
        </header>
    )
}