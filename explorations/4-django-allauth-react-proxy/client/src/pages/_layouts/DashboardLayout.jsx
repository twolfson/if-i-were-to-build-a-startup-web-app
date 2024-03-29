import assert from "assert";

export const DashboardLayout = ({ statusArr = [], children }) => {
  let content;

  if (statusArr.includes("loading")) {
    content = "Loading...";
  } else if (statusArr.includes("error")) {
    content = "An error occurred";
  } else {
    assert(
      statusArr
        // Filter out `null` statuses
        .filter((status) => !!status)
        // Sanity check the rest
        .every((status) => ["success", "idle"].includes(status)),
      `Unexpected status found in ${JSON.stringify(statusArr)}`,
    );
    content = children;
  }
  return <div id="content">{content}</div>;
};
