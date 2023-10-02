export default function InputField() {
  return (
    <div>
      <div className="col-span-6"></div>
      <div className="col-span-6 sm:col-span-3">
        <label
          htmlFor="first_name"
          className="block text-sm font-medium text-gray-700"
        >
          First name
        </label>
        <input
          type="text"
          name="first_name"
          id="first_name"
          autoComplete="given-name"
          className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
        />
        <input
          type="text"
          name="first_name"
          id="first_name"
          autoComplete="given-name"
          className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
        />
      </div>
      <div className="col-span-6 sm:col-span-3">
        <label
          htmlFor="last_name"
          className="block text-sm font-medium text-gray-700"
        >
          Last name
        </label>
        <input
          type="text"
          name="last_name"
          id="last_name"
          autoComplete="family-name"
          className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
        />
      </div>
    </div>
  );
}
