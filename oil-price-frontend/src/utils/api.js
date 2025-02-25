import axios from 'axios';

const API_URL = 'http://localhost:5000/api'; // Adjust based on your Flask server

export const getData = async () => {
    try {
        const response = await axios.get(`${API_URL}/data`);
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return [];
    }
};

export const getMetrics = async () => {
    try {
        const response = await axios.get(`${API_URL}/metrics`);
        return response.data;
    } catch (error) {
        console.error('Error fetching metrics:', error);
        return {};
    }
};

export const getEvents = async () => {
    try {
        const response = await axios.get(`${API_URL}/events`);
        return response.data;
    } catch (error) {
        console.error('Error fetching events:', error);
        return [];
    }
};
