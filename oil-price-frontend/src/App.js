import React from 'react';
import DataTable from './components/DataTable';
import EventList from './components/EventList';
import Metrics from './components/Metrics';
import PriceChart from './components/PriceChart';

const App = () => {
    return (
        <div>
            <h1>Oil Price Analysis</h1>
            <PriceChart />
            <DataTable />
            <EventList />
            <Metrics />
        </div>
    );
};

export default App;
