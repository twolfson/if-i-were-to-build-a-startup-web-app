import { BaseLayout } from "./_layouts/BaseLayout";

export const Index = () => {
  return (
    <BaseLayout>
      <h1>Hello World!</h1>
      <a href="/auth/logout">Logout</a>
    </BaseLayout>
  );
};
