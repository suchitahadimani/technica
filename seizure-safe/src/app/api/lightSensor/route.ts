import { NextResponse } from 'next/server';
import {SerialPort} from 'serialport';
import { ReadlineParser } from '@serialport/parser-readline';

const port = new SerialPort({
  path: '/dev/cu.SLAB_USBtoUART', // Adjust to your port
  baudRate: 9600,
});

const parser = port.pipe(new ReadlineParser({ delimiter: '\n' }));

export async function GET() {
    return new Promise((resolve, reject) => {
      parser.on('data', (data: string) => {
        console.log('Sensor value:', data);
        resolve(NextResponse.json({ value: data }));
      });
  
      port.on('error', (err: Error) => {
        console.error('Error: ', err.message);
        reject(NextResponse.json({ error: err.message }, { status: 500 }));
      });
    });
  }
