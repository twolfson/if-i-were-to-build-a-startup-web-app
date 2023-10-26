import { useQuery, useQueryClient } from "@tanstack/react-query";
const e = encodeURIComponent;

const MESSAGES_KEY = ["messages"];

export const useInvalidateMessages = () => {
  const queryClient = useQueryClient();
  return () => {
    queryClient.invalidateQueries({ queryKey: MESSAGES_KEY });
  };
};

export const useMessages = (options) => {
  return useQuery(
    MESSAGES_KEY,
    () =>
      fetch("/auth/messages/").then((res) => res.json()),
    options
  );
};

export const useUser = (id, options) => {
  return useQuery(
    ["users", id],
    () =>
      fetch(`/api/users/${e(id)}`).then((res) => res.json()),
    options
  );
};
