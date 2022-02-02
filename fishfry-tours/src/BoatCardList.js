import React from "react";
import { Card, Paper, Typography } from "@material-ui/core";

const BoatCard = ({ boatCard }) => {
    return (
        <div className="boat-card-item">
            <Card variant="outlined">
                {boatCard.name} {boatCard.status}
            </Card>
        </div>
    )
}

const BoatCardList = ({ boatCards }) => {
    const renderCard = (boatCard, index) => {
        return (
            <BoatCard boatCard={boatCard} key={index} />
        )
    }

    const dockedBoats = boatCards.filter((boat) => boat.status.toLowerCase() === 'docked')
    const maintenanceBoats = boatCards.filter((boat) => boat.status.toLowerCase() === 'maintenance')
    const outboundBoats = boatCards.filter((boat) => boat.status.toLowerCase().replace("_", " ") === 'outbound to sea')
    const inboundBoats = boatCards.filter((boat) => boat.status.toLowerCase().replace("_", " ") === 'inbound to harbour')

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