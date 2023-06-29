import { DashComponentProps } from "props";
import React, { useState } from "react";
type Props = {
  effectAllowed?: string;
  transferType?: string;
  name?: string;
} & DashComponentProps;

const DragFrom: React.FC<Props> = ({
  effectAllowed,
  transferType,
  name,
  children,
}) => {
  const onDragStart = (event, nodeType) => {
    event.dataTransfer.setData("text/x-tab-name", name);
    event.dataTransfer.effectAllowed = effectAllowed;
    console.log(event.dataTransfer);
  };

  return (
    <div
      className="dndnode input"
      onDragStart={(event) => onDragStart(event, "input")}
      draggable={true}
    >
      {children}
    </div>
  );
};

export default DragFrom;
