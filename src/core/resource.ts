// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import type { EricCompositiontar } from '../client';

export abstract class APIResource {
  protected _client: EricCompositiontar;

  constructor(client: EricCompositiontar) {
    this._client = client;
  }
}
