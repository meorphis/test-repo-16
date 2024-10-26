// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import Mixedbread, { toFile } from 'mixedbread';
import { Response } from 'node-fetch';

const client = new Mixedbread({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource files', () => {
  test('create: only required params', async () => {
    const responsePromise = client.files.create({
      file: await toFile(Buffer.from('# my file contents'), 'README.md'),
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('create: required and optional params', async () => {
    const response = await client.files.create({
      file: await toFile(Buffer.from('# my file contents'), 'README.md'),
    });
  });

  test('retrieve', async () => {
    const responsePromise = client.files.retrieve('file_id');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('retrieve: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(client.files.retrieve('file_id', { path: '/_stainless_unknown_path' })).rejects.toThrow(
      Mixedbread.NotFoundError,
    );
  });

  test('update: only required params', async () => {
    const responsePromise = client.files.update('file_id', {
      file: await toFile(Buffer.from('# my file contents'), 'README.md'),
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('update: required and optional params', async () => {
    const response = await client.files.update('file_id', {
      file: await toFile(Buffer.from('# my file contents'), 'README.md'),
    });
  });

  test('list', async () => {
    const responsePromise = client.files.list();
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('list: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(client.files.list({ path: '/_stainless_unknown_path' })).rejects.toThrow(
      Mixedbread.NotFoundError,
    );
  });

  test('list: request options and params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.files.list({ after: 'after', limit: 0 }, { path: '/_stainless_unknown_path' }),
    ).rejects.toThrow(Mixedbread.NotFoundError);
  });

  test('content: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(client.files.content('file_id', { path: '/_stainless_unknown_path' })).rejects.toThrow(
      Mixedbread.NotFoundError,
    );
  });

  test('del', async () => {
    const responsePromise = client.files.del('file_id');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('del: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(client.files.del('file_id', { path: '/_stainless_unknown_path' })).rejects.toThrow(
      Mixedbread.NotFoundError,
    );
  });
});
