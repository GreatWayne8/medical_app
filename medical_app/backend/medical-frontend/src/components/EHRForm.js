import React, { useEffect, useState } from "react";
import axios from "axios";

const EHRList = () => {
    const [records, setRecords] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/ehr/")
            .then(response => {
                setRecords(response.data);
            })
            .catch(error => {
                console.error("Error fetching EHR records:", error);
            });
    }, []);

    return (
        <div className="p-4">
            <h2 className="text-2xl font-bold mb-4">Electronic Health Records</h2>
            <table className="w-full border-collapse border border-gray-300">
                <thead>
                    <tr className="bg-gray-200">
                        <th className="border p-2">Patient</th>
                        <th className="border p-2">Doctor</th>
                        <th className="border p-2">Diagnosis</th>
                        <th className="border p-2">Prescriptions</th>
                    </tr>
                </thead>
                <tbody>
                    {records.map(record => (
                        <tr key={record.id}>
                            <td className="border p-2">{record.patient}</td>
                            <td className="border p-2">{record.doctor}</td>
                            <td className="border p-2">{record.diagnosis}</td>
                            <td className="border p-2">{record.prescriptions}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default EHRList;
