"use client"
import { useEffect, useState } from 'react';

export default function LightSensor() {
  const [lightValue, setLightValue] = useState<string | null>(null);

  useEffect(() => {
    const fetchLightData = async () => {
      try {
        const response = await fetch('/api/lightSensor');
        const data = await response.json();
        setLightValue(data.lightValue);
      } catch (error) {
        console.error('Error fetching light sensor data:', error);
      }
    };

    const interval = setInterval(fetchLightData, 1000); // Fetch data every second
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>Light Sensor Reading</h1>
      {lightValue ? <p>{lightValue}</p> : <p>Loading...</p>}
    </div>
  );
}
