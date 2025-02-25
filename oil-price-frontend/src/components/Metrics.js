import React, { useEffect, useState } from 'react';
import { getMetrics } from '../utils/api';

const Metrics = () => {
    const [metrics, setMetrics] = useState({});

    useEffect(() => {
        const fetchMetrics = async () => {
            const result = await getMetrics();
            setMetrics(result);
        };
        fetchMetrics();
    }, []);

    return (
        <div>
            <h2>Model Metrics</h2>
            <p>RMSE: {metrics.rmse}</p>
            <p>MAE: {metrics.mae}</p>
        </div>
    );
};

export default Metrics;
