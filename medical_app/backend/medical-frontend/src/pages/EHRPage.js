import React, { useState } from "react";
import EHRList from "../components/EHRList";
import EHRForm from "../components/EHRForm";

const EHRPage = () => {
    const [reload, setReload] = useState(false);

    const handleRecordAdded = () => {
        setReload(!reload);  // Triggers reload of EHR list
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-3xl font-bold text-center mb-6">EHR Management</h1>
            <EHRForm onRecordAdded={handleRecordAdded} />
            <EHRList key={reload} />
        </div>
    );
};

export default EHRPage;
