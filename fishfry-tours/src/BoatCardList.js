import React from "react";
import { Card, CardActions, CardContent, Paper, Typography } from "@material-ui/core";
import ClearIcon from '@mui/icons-material/Clear';
import { Button, IconButton } from "@mui/material";

const MaintenanceCard = ( boatCard, index, deleteBoat, updateBoat ) => {
    return (
        <div className={`maintenance-boat-card-${index}`}>
            <Card variant="outlined">
                <CardContent>
                    <Typography variant="h5">
                        {boatCard.name}
                    </Typography>
                </CardContent>
                <CardActions>
                    <IconButton onClick={() => deleteBoat(boatCard.id)}>
                        <ClearIcon />
                    </IconButton>
                    <Button onClick={() => updateBoat(boatCard.id, 'DOCKED')}>
                        Docked
                    </Button>
                    <Button onClick={() => updateBoat(boatCard.id, 'OUTBOUND_TO_SEA')}>
                        Outbound to Sea
                    </Button>
                    <Button onClick={() => updateBoat(boatCard.id, 'INBOUND_TO_HARBOUR')}>
                        Inbound to Harbour
                    </Button>
                </CardActions>
            </Card>
        </div>
    )
}

const OutboundCard = ( boatCard, index, deleteBoat, updateBoat ) => {
    return (
        <div className={`outbound-boat-card-${index}`}>
            <Card variant="outlined">
                <CardContent>
                    <Typography variant="h5">
                        {boatCard.name}
                    </Typography>
                </CardContent>
                <CardActions>
                    <IconButton onClick={() => deleteBoat(boatCard.id)}>
                        <ClearIcon />
                    </IconButton>
                    <Button onClick={() => updateBoat(boatCard.id, 'MAINTENANCE')}>
                        Maintenance
                    </Button>
                    <Button onClick={() => updateBoat(boatCard.id, 'INBOUND_TO_HARBOUR')}>
                        Inbound to Harbour
                    </Button>
                </CardActions>
            </Card>
        </div>
    )
}

const InboundCard = ( boatCard, index, deleteBoat, updateBoat ) => {
    return (
        <div className={`inbound-boat-card-${index}`}>
            <Card variant="outlined">
                <CardContent>
                    <Typography variant="h5">
                        {boatCard.name}
                    </Typography>
                </CardContent>
                <CardActions>
                    <IconButton onClick={() => deleteBoat(boatCard.id)}>
                        <ClearIcon />
                    </IconButton>
                    <Button onClick={() => updateBoat(boatCard.id, 'DOCKED')}>
                        Docked
                    </Button>
                    <Button onClick={() => updateBoat(boatCard.id, 'MAINTENANCE')}>
                        Maintenance
                    </Button>
                </CardActions>
            </Card>
        </div>
    )
}

const DockedCard = ( boatCard, index, deleteBoat, updateBoat ) => {
    return (
        <div className={`docked-boat-card-${index}`}>
            <Card variant="outlined">
                <CardContent>
                    <Typography variant="h5">
                        {boatCard.name}
                    </Typography>
                </CardContent>
                <CardActions>
                    <IconButton onClick={() => deleteBoat(boatCard.id)}>
                        <ClearIcon />
                    </IconButton>
                    <Button onClick={() => updateBoat(boatCard.id, 'MAINTENANCE')}>
                        Maintenance
                    </Button>
                    <Button onClick={() => updateBoat(boatCard.id, 'OUTBOUND_TO_SEA')}>
                        Outbound to Sea
                    </Button>
                </CardActions>
            </Card>
        </div>
    )
}

const BoatCard = ({ boatCard, deleteBoat, updateBoat, key }) => {
    if (boatCard.status.toLowerCase().replace(/_/g, " ") === 'docked') {
        return DockedCard(boatCard, key, deleteBoat, updateBoat)
    }
    if (boatCard.status.toLowerCase().replace(/_/g, " ") === 'maintenance') {
        return MaintenanceCard(boatCard, key, deleteBoat, updateBoat)
    }
    if (boatCard.status.toLowerCase().replace(/_/g, " ") === 'outbound to sea') {
        return OutboundCard(boatCard, key, deleteBoat, updateBoat)
    }
    if (boatCard.status.toLowerCase().replace(/_/g, " ") === 'inbound to harbour') {
        return InboundCard(boatCard, key, deleteBoat, updateBoat)
    }
}

const BoatCardList = ({ boatCards, deleteBoat, updateBoat }) => {
    const renderCard = (boatCard, index) => {
        return (
            <BoatCard boatCard={boatCard} deleteBoat={deleteBoat} updateBoat={updateBoat} key={index} />
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