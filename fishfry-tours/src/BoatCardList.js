import React from "react";
import { Card, CardActions, CardContent, Paper, Typography } from "@material-ui/core";
import ClearIcon from '@mui/icons-material/Clear';
import { IconButton } from "@mui/material";
import deleteBoat from './App'

const BoatCard = ({ boatCard, deleteBoat }) => {
    return (
        <div className="boat-card-item">
            <Card variant="outlined">
                <CardContent>
                    <Typography variant="h5">
                        {boatCard.name}
                    </Typography>
                    <Typography color="textSecondary">
                        {boatCard.status}
                    </Typography>
                </CardContent>
                <CardActions>
                <IconButton onClick={() => deleteBoat(boatCard.id)}>
                    <ClearIcon />
                </IconButton>
                </CardActions>
            </Card>
        </div>
    )
}

const BoatCardList = ({ boatCards, deleteBoat }) => {
    const renderCard = (boatCard, index) => {
        return (
            <BoatCard boatCard={boatCard} deleteBoat={deleteBoat} key={index} />
        )
    }

    const dockedBoats = boatCards.filter(boat => boat.status.toLowerCase() === 'docked')
    const maintenanceBoats = boatCards.filter(boat => boat.status.toLowerCase() === 'maintenance')
    const outboundBoats = boatCards.filter(boat => boat.status.toLowerCase().replace(/_/g, " ") === 'outbound to sea')
    const inboundBoats = boatCards.filter(boat => boat.status.toLowerCase().replace(/_/g, " ") === 'inbound to harbour')

    return (
        <Paper>
        <section className="docked-boat-card-list">
            <Paper>
            <Typography>
                <h1>DOCKED</h1>
            </Typography>
            {dockedBoats.map(renderCard)}
            </Paper>
        </section>
        <section className="maintenance-boat-card-list">
            <Paper>
                <Typography>
                    <h1>MAINTENANCE</h1>
                </Typography>
                {maintenanceBoats.map(renderCard)}
            </Paper>
        </section>
        <section className="outbound-boat-card-list">
            <Paper>
                <Typography>
                    <h1>OUTBOUND TO SEA</h1>
                </Typography>
                {outboundBoats.map(renderCard)}
            </Paper>
        </section>
        <section className="inbound-boat-card-list">
            <Paper>
                <Typography>
                    <h1>INBOUND TO HARBOUR</h1>
                </Typography>
                {inboundBoats.map(renderCard)}
            </Paper>
        </section>
        </Paper>
    )
}

export default BoatCardList