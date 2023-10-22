const e = encodeURIComponent;

export const useMessages = (options) => {
  return useQuery(
    ["messages"],
    () =>
      // TODO: Fetch isn't handling errors like 404 JSON parsing
      fetch("/auth/messages/").then((res) => res.json()),
    options
  );
};

export const useUser = (id, options) => {
  return useQuery(
    ["users", id],
    () =>
      // TODO: Fetch isn't handling errors like 404
      fetch(`/api/users/${e(id)}`).then((res) => res.json()),
    options
  );
};
