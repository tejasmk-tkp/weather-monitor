"use client";
import Image from "next/image";
import React, { useEffect, useState } from "react";

export default function Home() {
  const [stuff, setStuff] = useState(0);
  const [rainval, setRainVal] = useState(0);
  const [altitude, setAltitude] = useState(0);
  window.setTimeout(function () {
    window.location.reload();
    setStuff(Math.floor(Math.random()*1000));
    fetch("http://localhost:8000/rain_val/").then((res) => res.json()).then((data) => {
      setRainVal(data.rain_val);
      setAltitude(data.altitude);
    })
  }, 5000);
  return (
    <main className="grid place-items-center w-screen h-screen p-16">
      <div className="bg-sky-600 w-full h-full shadow-xl shadow-sky-900 rounded-3xl grid place-items-center">
        <div>
          <Image src={`http://localhost:8000/${stuff}`} width={800} height={800} alt="graph" />
          <div className="grid grid-cols-2">
            <p>Altitude: {altitude}</p>
            <p className="text-right">Rain Value: {rainval}</p>
          </div>
        </div>

      </div>
    </main>
  );
}
