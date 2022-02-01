import React from "react";
import { Card } from "@material-ui/core";

const BoatCard = ({ boatCard }) => {
    return (
        <div className="boat-card-item">
            <Card variant="outlined">
                {boatCard.name}
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

    return (
        <section className="boat-card-list">
            {boatCards.map(renderCard)}
        </section>
    )
}

export default BoatCardList