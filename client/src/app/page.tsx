"use client";
import React, { useState, useEffect } from "react";
import { Orbitron } from "next/font/google";
import { CartesianGrid, Line, LineChart, Tooltip, XAxis, YAxis } from "recharts";

const font = Orbitron({
  weight: "400",
  subsets: ["latin"],

})


export default function Page() {
  const [data, setData] = useState([
    { temperature: 0, humidity: 0, pressure: 0, altitude: 0, rain_value: 0 },
  ]);

  useEffect(() => {
    const interval = setInterval(() => {
      const API_URL = "http://127.0.0.1:8000/";
      fetch(API_URL + "data").then((res) => res.json()).then((d) => {
        setData(d);
        console.log(d)
      })
    }, 3000);
    return () => clearInterval(interval);
  }, []);


  return (
    <main className="">
      <div className="w-full h-full grid place-items-center p-16">
        <div className="grid grid-cols-2 gap-2 bg-sky-900 p-4 rounded-3xl w-full  shadow-xl">
          <div className="grid grid-cols-3 col-span-2 w-full h-full gap-2">
            <div className="bg-sky-950 w-full h-full rounded-xl p-4">
              <div className="grid place-items-center">
                <h1 className="text-4xl font-bold text-white">Temperature</h1>
                <h1 className="text-4xl  text-white">{data[data.length - 1].temperature}°C</h1>
              </div>
            </div>
            <div className="bg-sky-950 w-full h-full rounded-xl p-4">
              <div className="grid place-items-center">
                <h1 className="text-4xl font-bold text-white">Rain Value</h1>
                <h1 className="text-4xl  text-white">{data[data.length - 1].rain_value ? "yes":"no"}</h1>
              </div>

            </div>
            <div className="bg-sky-950 w-full h-full rounded-xl p-4">
              <div className="grid place-items-center">
                <h1 className="text-4xl font-bold text-white">Altitude</h1>
                <h1 className="text-4xl  text-white">{data[data.length - 1].altitude}m</h1>
              </div>
            </div>
          </div>
          <div className="bg-sky-950 rounded-2xl p-8 w-full">
            <LineChart width={800} height={400} data={data}>
              <Line type="monotone" dataKey="temperature" stroke="#8884d8" strokeWidth={4} />
              <YAxis />
              <CartesianGrid />
              <Tooltip />
              <XAxis dataKey="name" />
            </LineChart>
          </div>
          <div className="bg-sky-950 rounded-2xl p-8">
            <LineChart width={800} height={400} data={data}>
              <Line type="monotone" dataKey="humidity" stroke="#8884d8" strokeWidth={4} />
              <YAxis />
              <CartesianGrid />
              <Tooltip />
              <XAxis dataKey="name" />
            </LineChart>
          </div>
          <div className="bg-sky-950 rounded-2xl p-8">
            <LineChart width={800} height={400} data={data}>
              <Line type="monotone" dataKey="pressure" stroke="#8884d8" strokeWidth={4} />
              <YAxis />
              <CartesianGrid />
              <Tooltip />
              <XAxis dataKey="name" />
            </LineChart>
          </div>
          <div className="bg-sky-950 rounded-2xl p-8">
            <LineChart width={800} height={400} data={data}>
              <Line type="monotone" dataKey="altitude" stroke="#8884d8" strokeWidth={4} />
              <YAxis />
              <CartesianGrid />
              <Tooltip />
              <XAxis dataKey="name" />
            </LineChart>
          </div>
          <div className="bg-sky-950 rounded-2xl p-8 col-span-2 grid place-items-center">
            <LineChart width={1200} height={400} data={data}>
              <Line type="monotone" dataKey="rain_value" stroke="#8884d8" strokeWidth={4} />
              <YAxis />
              <CartesianGrid />
              <Tooltip />
              <XAxis dataKey="name" />
            </LineChart>
          </div>
        </div>
      </div>
    </main>
  );
}