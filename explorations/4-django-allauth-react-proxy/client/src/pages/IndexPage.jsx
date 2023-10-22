import { BaseLayout } from "./_layouts/BaseLayout";

export const IndexPage = () => {
  return (
    <BaseLayout>
      <h1>Hello World!</h1>
      <a href="/auth/logout">Logout</a>
    </BaseLayout>
  );
};
