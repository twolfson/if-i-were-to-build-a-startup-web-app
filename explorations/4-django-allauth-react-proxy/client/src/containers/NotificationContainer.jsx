import { ToastContainer, toast } from "react-toastify";
import { useEffect } from "react";
import { useQuery } from "react-query";

export const NotificationContainer = () => {
  const { error: messagesError, data: messagesData } = useQuery(
    "messages",
    () =>
      // TODO: Fetch isn't handling errors like 404
      fetch("/auth/messages/").then((res) => res.json()),
  );

  useEffect(() => {
    if (messagesError) {
      throw messagesError;
    }
    if (messagesData) {
      messagesData.messages.forEach((message) => {
        toast(message.message, { type: message.level_tag });
      });
    }
  }, [messagesError, messagesData]);

  return <ToastContainer position="top-center" />;
};
