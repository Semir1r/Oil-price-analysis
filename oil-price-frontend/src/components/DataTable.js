import React, { useEffect, useState } from 'react';
import { getData } from '../utils/api';

const DataTable = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await getData();
            setData(result);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h2>Oil Price Data</h2>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item, index) => (
                        <tr key={index}>
                            <td>{item.date}</td>
                            <td>{item.price}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default DataTable;
