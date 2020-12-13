# Open ID Connect Provider

### Allow including claims in id token
```
OIDC_IDTOKEN_INCLUDE_CLAIMS = True
```

### Retrieve list of JWK:
```
 curl localhost:8000/openid/jwks 
 
 {
    "keys": [
        {
            "kty": "RSA",
            "alg": "RS256",
            "use": "sig",
            "kid": "f15f6c6ac45526ba8ba3644877e34585",
            "n": "rwjpAylV007B4_rHAjJa5_cHAWVa6fxbJsuQTpYNsCqrJHqfc_VA3ftzksDmaIu4sLrk2pa6hOiFHvTXIkU-0q1B4AoH9plh9E1VzneqRi07V-cL6ZVY1uecoPqfrdMelYuCdf69dCD0B8vOh3bepI5wdohshnxvPFD0jXW-u2R5pgO_w3qr0NqOt3sFgsNGLjcLynTBReR8Eail66AhbLt9aoQNW-W6IfYSFP45-FAgh8xy4p6jhv3-K51R90_1QGS1u6XAJN8VZbd7d4nTNqYcfDUBZsqER_f1u0BK2hmqchKBB-_78y6_QCCibr3DVkseRqZV1xycfcqcR_MBPQ",
            "e": "AQAB"
        }
    ]
}

```

### Retrieve `openid-configuration`
``` 
curl localhost:8000/openid/.well-known/openid-configuration

{
    "issuer": "http://localhost:8000/openid",
    "authorization_endpoint": "http://localhost:8000/openid/authorize",
    "token_endpoint": "http://localhost:8000/openid/token",
    "userinfo_endpoint": "http://localhost:8000/openid/userinfo",
    "end_session_endpoint": "http://localhost:8000/openid/end-session",
    "introspection_endpoint": "http://localhost:8000/openid/introspect",
    "response_types_supported": [
        "code",
        "id_token",
        "id_token token",
        "code token",
        "code id_token",
        "code id_token token"
    ],
    "jwks_uri": "http://localhost:8000/openid/jwks",
    "id_token_signing_alg_values_supported": [
        "HS256",
        "RS256"
    ],
    "subject_types_supported": [
        "public"
    ],
    "token_endpoint_auth_methods_supported": [
        "client_secret_post",
        "client_secret_basic"
    ]
}

```

### Token introspection (Authorization Code Flow)
  - Create `Client` with `response_type=code`
  - Allow token introspection in `settings.py`
    ``` 
    OIDC_INTROSPECTION_VALIDATE_AUDIENCE_SCOPE = True
    ```
    
  - Add `token_introspection` and `<client_id>` to `Client` scope
    
  - Do introspection:
  ``` 
  curl -XPOST localhost:8000/openid/introspect \
  -u <client_id>:<client_secret> \
  -d "token=<access_token>" 
  
  {
    "aud": "<client_id>",
    "sub": "1",
    "exp": 1607893872,
    "iat": 1607893272,
    "iss": "http://localhost:8000/openid",
    "active": true,
    "client_id": "<client_id>"
  }
  ```
