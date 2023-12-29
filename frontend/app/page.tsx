"use client"

import { useEffect, useState } from "react";
const orgid = 4729374

export default function Home() {
  const [apiData, setApiData] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`/api/data/`);
        const data = await response.json();
        setApiData(data)
        return data
      } catch (error) {
        console.error('Error fetching data', error);
      }
    };

    fetchData();
  }, []);


  console.log({apiData});
  return (
    <div className="w-8 bg-red-600 ">
      DOKU LABS
    </div>
  )
}
