import React from 'react';

const Row = () => {
    return (
        <div className="form-row">
            <div className="form-group col-md-3">
                <label className="form-label">Column Name</label>
                <input type="text" className="form-control" placeholder="Column Name" />
            </div>
            <div className="form-group col-md-3">
                <label className="form-label">Type</label>
                <select className="form-control" aria-label="Select Type">
                    <option selected>Select Type</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                </select>
            </div>
            <div className="form-row col-md-3">
                <div className="form-group col-md-6">
                    <label className="form-label">From</label>
                    <input type="number" className="form-control" placeholder="From" />
                </div>

                <div className="form-group col-md-6">
                    <label className="form-label">To</label>
                    <input type="number" className="form-control" placeholder="To" />
                </div>
            </div>
            <div className="form-group col-md-3">
                <a href="javascript:;">Delete</a>
            </div>
        </div>
    );
};

export default Row;