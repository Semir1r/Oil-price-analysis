import React, { useEffect, useState } from 'react';
import { getEvents } from '../utils/api';

const EventList = () => {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        const fetchEvents = async () => {
            const result = await getEvents();
            setEvents(result);
        };
        fetchEvents();
    }, []);

    return (
        <div>
            <h2>Significant Events</h2>
            <ul>
                {events.map((event, index) => (
                    <li key={index}>
                        <strong>{event.date}:</strong> {event.description}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default EventList;
